package edu.csumb.cst438.router;

import android.util.Log;

import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;

/**
 * Created by pico on 10/15/16.
 */

public class Connector {

    public SQLiteHelper.DeBra dbUtil;
    URL url;
    HttpURLConnection conn;
    static String AWS = "http://router-dev.us-west-2.elasticbeanstalk.com";
    static String checkLogin = "/checkLogin/";
    static String downloadRoute = "/downloadRoute/";
    static String uploadRoute = "/uploadRoute/";
    static String createUser = "/createUser/";
    static String getNearMe = "/getNearMe/";


    public Connector() {
        dbUtil = SQLiteHelper.DeBra.getInstance();

        try {
            conn = buildConnection("");
        }
        catch (Exception e) {
            Log.e("error", e.toString());
        }
    }

    private HttpURLConnection buildConnection(String endpoint) {
        try {
            url = new URL(AWS + endpoint);
            conn = (HttpURLConnection) url.openConnection();
            conn.setDoOutput(true);
            conn.setRequestMethod("POST");
            conn.setRequestProperty("Content-Type", "application/json");
        }
        catch (Exception e) {
            Log.e("error", e.toString());
        }

        return conn;
    }

    private String getResponse(String json, String endpoint) {
        try {
            conn = buildConnection(endpoint);
            OutputStream os = conn.getOutputStream();
            os.write(json.getBytes());
            os.flush();

            if (conn.getResponseCode() != HttpURLConnection.HTTP_CREATED) {
                throw new RuntimeException("Failed to connect: Code " + conn.getResponseCode());
            }

            BufferedReader br = new BufferedReader(new InputStreamReader(conn.getInputStream()));
            String response = "";
            while ((response += br.readLine()) != null)
                ; // will keep appending the json response to response var

            conn.disconnect();
            return response;
        } catch (Exception e) {
            Log.e("error", e.toString());
        }
        return "";
    }

    public static String sha1(String item) {
        byte[] b = item.getBytes();
        String result = "";
        for(int i = 0; i < item.length(); i++) {
            result += Integer.toString((b[i] & 0xff) + 0x100, 16).substring(1);
        }
        return result;
    }

    public int createUser(String username, String password) {
        password = sha1(password);
        String json = "";
        try {
            json = (new JSONObject()
                    .put("username", username)
                    .put("password", password)).toString();
        }
        catch (Exception e) {
            Log.d("error", e.toString());
        }

        try {
            JSONObject response = new JSONObject(getResponse(json.toString(), createUser));
            return Integer.parseInt((response.get("userid").toString()));
        }
        catch (Exception e) {
            Log.e("error", e.toString());
        }
        return -1;
    }

    public Boolean checkLogin(String username, String password) {
        password = sha1(password);
        String json = "";
        try {
            json = (new JSONObject()
                    .put("username", username)
                    .put("password", password)).toString();
        }
        catch (Exception e) {
            Log.d("error", e.toString());
        }

        try {
            JSONObject response = new JSONObject(getResponse(json.toString(), checkLogin));
            if(response.get("status") == "success") {
                return true;
            }
            return false;
        }
        catch (Exception e) {
            Log.e("error", e.toString());
        }

        return false;

    }
}
