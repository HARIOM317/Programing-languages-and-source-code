import javax.swing.*;

public class Swing_JButton_with_icon {
    Swing_JButton_with_icon(){
        JFrame f = new JFrame("Creating button with icon");
        JButton b = new JButton(new ImageIcon("A:\\Programming\\Java Tutorial\\Swing\\button.png"));
        b.setBounds(100, 100, 65, 65);
        f.add(b);
        f.setSize(300, 400);
        f.setLayout(null);
        f.setVisible(true);
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);   // to close the app with close button
    }

    public static void main(String[] args) {
        new Swing_JButton_with_icon();
    }
}
