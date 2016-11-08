package edu.csumb.cst438.router;

import android.content.ContentValues;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;

import java.util.ArrayList;

/**
 * Created by pico on 11/3/16.
 */

public class DeBra {

    public static SQLiteDatabase dbwrite;

    public DeBra(SQLiteDatabase db) {

        dbwrite = db;
    }



    public void insertRoute(Route route) {

        final ContentValues values = new ContentValues();
        values.put(SQLiteHelper.Routes.COLLUMN_NAME_ROUTEID, route.getRouteIdRemote());
        values.put(SQLiteHelper.Routes.COLLUMN_NAME_ROUTE, route.getRoute());
        values.put(SQLiteHelper.Routes.COLLUMN_NAME_ROUTE_NAME, route.getRouteName());
        values.put(SQLiteHelper.Routes.COLLUMN_NAME_START_POINT_LAT, route.getStartPointLat());
        values.put(SQLiteHelper.Routes.COLLUMN_NAME_START_POINT_LON, route.getStartPointLon());
        values.put(SQLiteHelper.Routes.COLLUMN_NAME_USER_ID, route.getUserId());

        insert(SQLiteHelper.Routes.TABLE_NAME, values);

    }

    public void deleteRoute(int id) {
        String query = String.format("DELETE FROM Routes WHERE RouteId = %s", Integer.toString(id));
        dbwrite.execSQL(query);
    }

    private void rawQuery(final String query) {
        dbwrite.rawQuery(query, null);
    }


    private void insert(final String tableName, final ContentValues values) {
        new Thread(new Runnable() {
            @Override
            public void run() {
                dbwrite.insert(tableName, "null", values);
            }
        }).start();
    }

    public Route getRouteById(int id) {
        String query = String.format("SELECT * FROM Routes WHERE RouteId = %s", id);

        Cursor c = dbwrite.rawQuery(query, null);

        if(c.getCount() == 0) { return null; }

        c.moveToFirst();

        // _id, RouteId, Route, StartPointLat, StartPointLon, RouteName, UserId
        return new Route(false, c.getInt(1), c.getString(2), c.getString(3), c.getString(4), c.getInt(6), c.getString(5));
    }

    public void update(final String query) {
        new Thread(new Runnable() {
            @Override
            public void run() {
                dbwrite.rawQuery(query, null);
            }
        }).start();
    }

    public ArrayList<Route> getAllLocalRoutes() {
        String query = "SELECT * FROM Routes WHERE 1";

        ArrayList<Route> routes = new ArrayList<>();

        Cursor c = dbwrite.rawQuery(query, null);

        c.moveToFirst();
        while(c.moveToNext()) {
            routes.add(new Route(false, c.getInt(1), c.getString(2), c.getString(3), c.getString(4), c.getInt(6), c.getString(5)));
        }

        return routes;
    }
}
