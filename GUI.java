import java.awt.EventQueue;

import javax.swing.JFrame;
import java.awt.Color;
import javax.swing.JLabel;
import javax.swing.SwingConstants;
import java.awt.Font;
import javax.swing.JTextField;
import javax.swing.JTextArea;
import javax.swing.JScrollPane;
import javax.swing.JButton;
import java.awt.event.ActionListener;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.awt.event.ActionEvent;

public class GUI {

	private JFrame frame;
	private JTextField query;
	private JTextField countryCode;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					GUI window = new GUI();
					window.frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the application.
	 */
	public GUI() {
		initialize();
	}

	/**
	 * Initialize the contents of the frame.
	 */
	private void initialize() {
		frame = new JFrame();
		frame.getContentPane().setBackground(new Color(103, 190, 237));
		frame.getContentPane().setForeground(new Color(103, 190, 237));
		frame.setBounds(100, 100, 653, 435);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.getContentPane().setLayout(null);
		
		JLabel lblNewLabel = new JLabel("InstagramGraphCrawler");
		lblNewLabel.setFont(new Font("Segoe Print", Font.BOLD, 25));
		lblNewLabel.setHorizontalAlignment(SwingConstants.CENTER);
		lblNewLabel.setBounds(10, 10, 619, 38);
		frame.getContentPane().add(lblNewLabel);
		
		query = new JTextField();
		query.setBackground(new Color(36, 162, 230));
		query.setBounds(27, 117, 182, 35);
		query.setFont(new Font("Segoe Print", Font.BOLD, 15));
		frame.getContentPane().add(query);
		query.setColumns(10);
		
		JLabel lblNewLabel_1 = new JLabel("Graph Name");
		lblNewLabel_1.setToolTipText("name of graph your trying to look for");
		lblNewLabel_1.setFont(new Font("Segoe Print", Font.BOLD, 15));
		lblNewLabel_1.setHorizontalAlignment(SwingConstants.CENTER);
		lblNewLabel_1.setBounds(27, 77, 180, 30);
		frame.getContentPane().add(lblNewLabel_1);
		
		JLabel lblNewLabel_1_1 = new JLabel("Country Code");
		lblNewLabel_1_1.setToolTipText("country code, example: canada is CA, while USA is US");
		lblNewLabel_1_1.setHorizontalAlignment(SwingConstants.CENTER);
		lblNewLabel_1_1.setFont(new Font("Segoe Print", Font.BOLD, 15));
		lblNewLabel_1_1.setBounds(27, 174, 180, 30);
		frame.getContentPane().add(lblNewLabel_1_1);
		
		countryCode = new JTextField();
		countryCode.setColumns(10);
		countryCode.setBackground(new Color(36, 162, 230));
		countryCode.setBounds(27, 214, 182, 35);
		countryCode.setFont(new Font("Segoe Print", Font.BOLD, 15));
		frame.getContentPane().add(countryCode);
		
		JScrollPane scrollPane = new JScrollPane();
		scrollPane.setBounds(300, 117, 329, 271);
		frame.getContentPane().add(scrollPane);
		
		final JTextArea logs = new JTextArea();
		scrollPane.setViewportView(logs);
		logs.setEditable(false);
		logs.setBackground(new Color(192, 192, 192));
		
		JLabel lblNewLabel_1_2 = new JLabel("Logs");
		lblNewLabel_1_2.setToolTipText("name of graph your trying to look for");
		lblNewLabel_1_2.setHorizontalAlignment(SwingConstants.CENTER);
		lblNewLabel_1_2.setFont(new Font("Segoe Print", Font.BOLD, 20));
		lblNewLabel_1_2.setBounds(300, 77, 329, 30);
		frame.getContentPane().add(lblNewLabel_1_2);
		
		JButton submit = new JButton("submit");
		submit.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				
				logs.setText(null);
				
				String querys = query.getText();
				String country = countryCode.getText();

				// Construct the command and arguments as an array of strings
				String[] command = { "python", "dataExtraction.py", "--query", querys, "--location", country };

				try {
				    ProcessBuilder builder = new ProcessBuilder(command);
				    Process process = builder.start();

				    BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
				    BufferedReader errorReader = new BufferedReader(new InputStreamReader(process.getErrorStream()));

				    String line;

				    while ((line = reader.readLine()) != null) {
				        if (!line.trim().isEmpty()) {
				            System.out.println(line); // Output or process non-empty lines
				            logs.append("[LOG] : " + line + "\n");
				        }
				    }

				    while ((line = errorReader.readLine()) != null) {
				        if (!line.trim().isEmpty()) {
				            System.out.println("Error: " + line); // Output or process non-empty error lines
				            logs.append("[ERROR] : " + line + "\n");
				        }
				    }
				} catch (Exception error) {
				    System.out.println(error);
				}
				
			}
		});
		submit.setForeground(new Color(0, 0, 0));
		submit.setBackground(new Color(192, 192, 192));
		submit.setFont(new Font("Segoe Print", Font.BOLD, 20));
		submit.setBounds(27, 279, 182, 38);
		frame.getContentPane().add(submit);
	}
}
