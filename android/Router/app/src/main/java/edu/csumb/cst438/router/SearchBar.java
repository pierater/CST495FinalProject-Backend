package edu.csumb.cst438.router;

import android.content.Context;
import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

public class SearchBar extends Fragment {

    public SearchBar() {
    }

    //This method allows an activity to add this fragment dynamically
    public static SearchBar newInstance() {
        return new SearchBar();
    }

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        return inflater.inflate(R.layout.fragment_search_bar, container, false);
    }

    @Override
    public void onDetach() {
        super.onDetach();
    }
}
