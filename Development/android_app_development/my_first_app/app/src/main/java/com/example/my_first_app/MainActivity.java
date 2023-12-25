package com.example.my_first_app;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    public void sendNow(View view){
        Toast.makeText(this, "Message sent successfully!", Toast.LENGTH_SHORT).show();
    }

    public void receiveNow(View view){
        Toast.makeText(this, "Message received successfully!", Toast.LENGTH_SHORT).show();
    }

    public void deleteNow(View view){
        Toast.makeText(this, "Message deleted successfully!", Toast.LENGTH_SHORT).show();
    }



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }
}