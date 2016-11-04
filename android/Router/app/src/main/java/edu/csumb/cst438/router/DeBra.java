package edu.csumb.cst438.router;

import android.content.ContentValues;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;

/**
 * Created by pico on 11/3/16.
 */

public class DeBra {

    private Application app;
    public static SQLiteDatabase dbwrite;
    public static SQLiteDatabase dbread;

    public DeBra(Application app) {
        this.app = app;

        dbwrite = app.getDbwrite();
        dbread = app.getDbread();
    }



    public void insertRoute(String routeId, String route, String routeName, String startLat, String startLon, String userId) {

        final ContentValues values = new ContentValues();
        values.put(SQLiteHelper.Routes.COLLUMN_NAME_ROUTEID, routeId);
        values.put(SQLiteHelper.Routes.COLLUMN_NAME_ROUTE, route);
        values.put(SQLiteHelper.Routes.COLLUMN_NAME_ROUTE_NAME, routeName);
        values.put(SQLiteHelper.Routes.COLLUMN_NAME_START_POINT_LAT, startLat);
        values.put(SQLiteHelper.Routes.COLLUMN_NAME_START_POINT_LON, startLon);
        values.put(SQLiteHelper.Routes.COLLUMN_NAME_USER_ID, userId);

        insert(SQLiteHelper.Routes.TABLE_NAME, values);

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

        Cursor c = dbread.rawQuery(query, null);

        if(c.getCount() == 0) { return null; }

        return new Route(false, c.getInt(1), c.getString(2), c.getString(3), c.getString(4), c.getInt(6), c.getString(7));
    }

}
