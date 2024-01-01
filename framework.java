package gui;

import java.io.BufferedReader;
import java.io.InputStreamReader; // Importing InputStreamReader

public class gui {
	public static void main(String[] args) {

		try {

			String query = "crime rate";

			ProcessBuilder builder = new ProcessBuilder("python", "dataExtraction.py", "--query", query, "--location", "CA");
			Process process = builder.start();

			BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
			BufferedReader readers = new BufferedReader(new InputStreamReader(process.getErrorStream()));

			String lines = null;

			while ((lines = reader.readLine()) != null) {
				if (!lines.trim().isEmpty()) {
					System.out.println(lines); // Do something with the non-empty line
				}
			}

			while ((lines = readers.readLine()) != null) {
				if (!lines.trim().isEmpty()) {
					System.out.println(lines); // Do something with the non-empty line
				}
			}


		} catch (Exception e) {
			System.out.println(e);
		}
	}
}
