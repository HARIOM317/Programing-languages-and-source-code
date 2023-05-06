import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Swing_JButton {
    public static void main(String[] args) {
        JFrame f=new JFrame();//creating instance of JFrame
        JTextField tf = new JTextField();
        tf.setBounds(50, 20, 200, 50);

        JButton b=new JButton("click");//creating instance of JButton
        b.setBounds(100,100,100, 50);//x-axis, y-axis, width, height
        b.setSize(100,50);

        // void addActionListener() - It is used to add the action listener to this object.
        b.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                tf.setText("Clicked the button!");
            }
        });
        f.add(b);//adding button in JFrame
        f.add(tf);

        f.setSize(400,500);//400 width and 500 height
        f.setLayout(null);//using no layout managers
        f.setVisible(true);//making the frame visible
    }
}
