# InstagramGraphCrawler: Instagram Graph Posting Tool

Python-based tool make to automate the process of fetching data based on user queries, generating a graph based off that, and swiftely posting them on Instagram. The repo uses a set of scripts to automate the data extraction, graph generation, conversion, and posting on Instagram.

## Key Features:

- **Data Extraction**: Utilizes the World Bank API to retrieve data based on user-defined queries and locations.
- **Graph Generation**: Processes fetched data to create graphical representations using Pandas and Matplotlib libraries.
- **Image Conversion**: Converts generated graphs into Instagram compatible JPEG format.
- **Instagram Posting**: Enables seamless login to an Instagram account and facilitates posting the refined graphs with captions.

## How to Use:

1. **Setup**:
   - use following command to install required dependencies
     ```
     pip install -r requirements. txt
     ```
   - Configure `credentials.json` with your Instagram login details.

2. **Usage**:
   - there are 2 ways to run the program, you can use the `runner.bat` to run the scripts for you,
   - Alternatively you can just run `main.py` with the `--query` and `--location` arguments to initiate the entire process.
     ```
     python main.py --query "YourQueryHere" --location "YourLocationHere"
     ```
   - Follow prompts to confirm caption and proceed with the Instagram post.

## Repository Contents:

- `dataExtraction.py`: does data retrieval and graph generation.
- `instagram.py`: does Instagram login, posting functionality, and conversion to jpeg image file.
- `main.py`: Main file running the each script in proper order using provided querys.
- `credentials.json`: contains the login information required to login into the account and post the graph.
- `runner.bat`: batch file which can run the files for you, will ask for 2 inputs from the user.

## Note:

- Customize queries and locations for specific data and graphs.
- Adjustments to the code may be needed for personalized data representation.
- Ensure adherence to Instagram's posting policies and guidelines.

## License:

This project is licensed under the [MIT License](LICENSE).
