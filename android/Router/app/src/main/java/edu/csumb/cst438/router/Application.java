package edu.csumb.cst438.router;

import android.database.sqlite.SQLiteDatabase;
import android.util.Log;

import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

/**
 * Created by pico on 11/1/16.
 */

public class Application extends android.app.Application {

    public static SQLiteHelper.DeBra dbUtil;
    public static SQLiteDatabase dbwrite;
    public static SQLiteDatabase dbread;
    public boolean readyToGo = false;

    final Lock lock = new ReentrantLock();
    final Condition notNull = lock.newCondition();
    final Condition ready = lock.newCondition();

    public Application() {
        instantiate();
    }

    public void instantiate() {
        new Thread(new Runnable() {
            @Override
            public void run() {
                setUpDbUtil();
            }
        }).start();
        new Thread(new Runnable() {
            @Override
            public void run() {
                setUpReadWrite();
            }
        }).start();
    }

    private void setUpDbUtil() {
        lock.lock();

        try {
            dbUtil = SQLiteHelper.DeBra.getInstance();
            notNull.signal();
            Log.d("Application", "Signaled to set up read write");

            while (dbread == null && dbwrite == null) {
                ready.wait();
            }
            Log.d("Application", "dbread, dbwrite, dbUtil are ready");
            readyToGo = true;
        }
        catch (InterruptedException e) {
            Log.e("Application", e.toString());
        }
        lock.unlock();
    }

    private void setUpReadWrite() {
        lock.lock();

        try {
            while(dbUtil == null) {
                notNull.wait();
            }
            dbwrite = dbUtil.getWritableDatabase();
            dbread = dbUtil.getReadableDatabase();

            Log.d("Application", "setUpReadWrite done");
            ready.signal();

        }
        catch (InterruptedException e) {
            Log.e("Application", e.toString());
        }
    }

    public SQLiteDatabase getDbwrite() {
        return dbwrite;
    }

    public SQLiteDatabase getDbread() {
        return dbread;
    }
}
