package edu.csumb.cst438.router;

import android.database.sqlite.SQLiteDatabase;
import android.util.Log;

/**
 * Created by pico on 11/1/16.
 */

public class Application extends android.app.Application {

    public static SQLiteHelper.DeBra dbUtil;
    public static SQLiteDatabase dbwrite;
    public static SQLiteDatabase dbread;


    private Object lock = new Object();


    public Application() {
        instantiate();
    }

    public void instantiate() {
        Log.d("Application", "start first");
        new Thread(new Runnable() {
            @Override
            public void run() {
                setUpDbUtil();
            }
        }).start();

        Log.d("Application", "start second");
        new Thread(new Runnable() {
            @Override
            public void run() {
                setUpReadWrite();
            }
        }).start();
    }

    private void setUpDbUtil() {

        Log.d("Application", "Signaled to set up read write");
        dbUtil = SQLiteHelper.DeBra.getInstance();

        synchronized (lock) {


            lock.notify();
        }

        Log.d("Application", "dbread, dbwrite, dbUtil are ready");
    }

    private void setUpReadWrite() {
        Log.d("Application", "0");
        synchronized (lock) {
            while (dbUtil == null) {
                Log.d("Application", "1");
                try {
                    Log.d("Application", "2");
                    lock.wait();
                    Log.d("Application", "3");
                }
                catch (Exception e) {
                    Log.e("Application", e.toString());
                }
                Log.d("Application", "4");

            }
            Log.d("Application", "Ready to instance them");

            dbwrite = dbUtil.getWritableDatabase();
            dbread = dbUtil.getReadableDatabase();

            Log.d("Application", "setUpReadWrite done");
        }
    }

    public SQLiteDatabase getDbwrite() {
        return dbwrite;
    }

    public SQLiteDatabase getDbread() {
        return dbread;
    }
}
