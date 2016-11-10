package edu.csumb.cst438.router;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import com.daimajia.swipe.SimpleSwipeListener;
import com.daimajia.swipe.SwipeLayout;
import com.daimajia.swipe.adapters.BaseSwipeAdapter;

/**
 * Created by Pearce on 11/6/16.
 */

public class ListViewAdaptor extends BaseSwipeAdapter {

    private Context mContext;

    public ListViewAdaptor(Context context) {
        this.mContext = context;
    }

    @Override
    public int getSwipeLayoutResourceId(int position) {
        return R.id.swiper;
    }

    @Override
    public View generateView(int position, ViewGroup parent) {
        View v = LayoutInflater.from(mContext).inflate(R.layout.swiper, null);
        SwipeLayout swipeLayout = (SwipeLayout)v.findViewById(getSwipeLayoutResourceId(position));
        swipeLayout.addSwipeListener(new SimpleSwipeListener());
        // TODO add click listeners for the buttons revealed by swipe
        return v;
    }

    @Override
    public void fillValues(int position, View convertView) {
        TextView t = (TextView)convertView.findViewById(R.id.swiperRow);
        t.setText((position + 1) + ".");
    }

    @Override
    public int getCount() {
        return -1;
    }

    @Override
    public Object getItem(int position) {
        return null;
    }

    @Override
    public long getItemId(int position) {
        return position;
    }
}
