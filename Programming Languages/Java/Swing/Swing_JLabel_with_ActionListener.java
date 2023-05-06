import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Swing_JLabel_with_ActionListener extends Frame implements ActionListener {
    JTextField jTextField;
    JLabel jLabel;
    JButton jButton;

    Swing_JLabel_with_ActionListener(){
        jTextField = new JTextField("Hariom Singh Rajput");
        jTextField.setBounds(50, 100, 150, 30);

        jLabel = new JLabel();
        jLabel.setBounds(50, 150, 250, 30);

        jButton = new JButton("Show Name");
        jButton.setBounds(50, 200, 120, 35);

        jButton.addActionListener(this);
        add(jButton);
        add(jTextField);
        add(jLabel);

        setSize(400, 400);
        setLayout(null);
        setVisible(true);
    }

    public void actionPerformed(ActionEvent e){
        try {
            String name = jTextField.getText();
            jLabel.setText("My name is : "+name);
        }
        catch (Exception exception){
            System.out.println(exception);
        }
    }

    public static void main(String[] args) {
        new Swing_JLabel_with_ActionListener();
    }
}
