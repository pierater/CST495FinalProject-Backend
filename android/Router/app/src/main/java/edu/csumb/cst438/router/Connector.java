package edu.csumb.cst438.router;

import android.util.Log;

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


    public Connector() {
        dbUtil = SQLiteHelper.DeBra.getInstance();

        try {
            url = new URL("http://url.com:5000/root");
            conn = (HttpURLConnection) url.openConnection();
            conn.setDoOutput(true);
            conn.setRequestMethod("POST");
            conn.setRequestProperty("Content-Type", "application/json");
        }
        catch (Exception e) {
            Log.e("error", e.toString());
        }

    }

    private String getResponse(String json) {
        try {
            OutputStream os = conn.getOutputStream();
            os.write(json.getBytes());
            os.flush();

            if(conn.getResponseCode() != HttpURLConnection.HTTP_CREATED) {
                throw new RuntimeException("Failed to connect: Code " + conn.getResponseCode());
            }

            BufferedReader br = new BufferedReader(new InputStreamReader(conn.getInputStream()));
            String response = "";
            while((response += br.readLine()) != null); // will keep appending the json response to response var

            conn.disconnect();
            return response;
        }
        catch (Exception e) {
            Log.e("error", e.toString());
        }


    }

    
}
