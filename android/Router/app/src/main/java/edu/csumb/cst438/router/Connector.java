package edu.csumb.cst438.router;

/**
 * Created by pico on 10/15/16.
 */

public class Connector {

    public SQLiteHelper.DeBra dbUtil;

    public Connector() {
        dbUtil = SQLiteHelper.DeBra.getInstance();
    }

    
}
