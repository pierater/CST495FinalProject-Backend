package edu.csumb.cst438.router;


import android.content.Intent;
import android.support.design.widget.Snackbar;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import com.google.android.gms.auth.api.Auth;
import com.google.android.gms.auth.api.signin.GoogleSignInOptions;
import com.google.android.gms.auth.api.signin.GoogleSignInResult;
import com.google.android.gms.common.ConnectionResult;
import com.google.android.gms.common.SignInButton;
import com.google.android.gms.common.api.GoogleApiClient;

public class Login extends AppCompatActivity implements GoogleApiClient.OnConnectionFailedListener{
    private static final String TAG = "SignInActivity";
    private static final int RC_SIGN_IN = 9001;

    private EditText username_to_login;
    private EditText password_to_login;
    private Button login_button;
    private SignInButton signInButton;
    private GoogleApiClient mGoogleApiClient;
    private TextView mStatusTextView;
    private Connector connector = new Connector();


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);
        setupVariables();
        //  Configure sign-in to request the user's ID, email address, and basic profile. ID and
        //  basic profile are included in DEFAULT_SIGN_IN.
        GoogleSignInOptions gso = new GoogleSignInOptions.Builder(GoogleSignInOptions.DEFAULT_SIGN_IN)
                .requestEmail()
                .build();

        // Build a GoogleApiClient with access to GoogleSignIn.API and the options above.
        mGoogleApiClient = new GoogleApiClient.Builder(this)
                .enableAutoManage(this /* FragmentActivity */, this /* OnConnectionFailedListener */)
                .addApi(Auth.GOOGLE_SIGN_IN_API, gso)
                .build();

        signInButton.setSize(SignInButton.SIZE_STANDARD);
        signInButton.setScopes(gso.getScopeArray());

        login_button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String username = username_to_login.getText().toString();
                String password = password_to_login.getText().toString();

                if (username.trim().length() > 0 && password.trim().length() > 0) {
                    authenticateLogin(username, password);
                } else {
                    Snackbar.make(v, "Please Enter Credentials!", Snackbar.LENGTH_LONG)
                            .show();
                }
            }
        });

        signInButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
               signIn();
            }
        });
    }

    // [START onActivityResult]
    @Override
    public void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);

        // Result returned from launching the Intent from GoogleSignInApi.getSignInIntent(...);
        if (requestCode == RC_SIGN_IN) {
            GoogleSignInResult result = Auth.GoogleSignInApi.getSignInResultFromIntent(data);
            handleSignInResult(result);
        }
    }
    // [END onActivityResult]

    // [START handleSignInResult]
    private void handleSignInResult(GoogleSignInResult result) {
        Log.d(TAG, "handleSignInResult:" + result.isSuccess());
        if (result.isSuccess()) {
            Log.d(TAG, "signed in: success");

        } else {
            Log.d(TAG, "signed in: failed");
        }
    }

    private void signIn() {
        Intent signInIntent = Auth.GoogleSignInApi.getSignInIntent(mGoogleApiClient);
        startActivityForResult(signInIntent, RC_SIGN_IN);
    }

    @Override
    public void onConnectionFailed(ConnectionResult connectionResult) {
        // An unresolvable error has occurred and Google APIs (including Sign-In) will not
        // be available.
        Log.d(TAG, "onConnectionFailed:" + connectionResult);
    }

    public void logIn(View view) {
        connector.checkLogin(username_to_login.toString(), password_to_login.toString());
    }

    public void authenticateLogin(final String username, final String password) {

        new Thread(new Runnable() {
            @Override
            public void run() {
                //boolean result = connector.checkLogin(username, password);
                //int result = connector.createUser("username", "pass123", "mybio", "email@mail.com");
                int result = connector.uploadRoute(1, "lattitude", "longitude", "AWSOME ROUTE1", "just making sure");
                Log.d("upload", Integer.toString(result));
                //Log.d("create", Integer.toString(result));
                //Log.d("login", Boolean.toString(result));
            }
        }).start();


    }

    public void createUser(final String username, final String password, final String bio, final String email) {
        new Thread(new Runnable() {
            @Override
            public void run() {
                int userId = connector.createUser(username, password, bio, email);
                Log.d("create", Integer.toString(userId));
            }
        }).run();
    }

    private void setupVariables() {
        username_to_login = (EditText) findViewById(R.id.username_to_login);
        password_to_login = (EditText) findViewById(R.id.password_to_login);
        login_button = (Button) findViewById(R.id.login_button);
        signInButton = (SignInButton) findViewById(R.id.sign_in_button);
    }

    public void sendCreds() {

    }
}
