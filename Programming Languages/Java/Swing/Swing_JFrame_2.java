import javax.swing.*;

public class Swing_JFrame_2 extends JFrame {
    Swing_JFrame_2(){
        setTitle("Creating frame by extending JFrame");     // setting title
        setLayout(null);
        setSize(600,500);
        setVisible(true);
    }
    public static void main(String[] args) {
        new Swing_JFrame_2();
    }
}
