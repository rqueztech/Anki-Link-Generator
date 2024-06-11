# PyAutoGui portion:
This portion is not to be reused. Simply controls the GUI based on specific titles to automate the process of updating links.

# Japanese Linkifier Text Processing PowerShell Script

This PowerShell script processes Japanese text input provided by the user, utilizing various functionalities to enhance the user experience. It primarily focuses on identifying Japanese characters (Katakana, Hiragana, and Kanji) and providing useful links for further exploration and translation.

## Features

### 1. Japanese Character Validation

The script provides a function `ContainsOnlyJapaneseCharacters` to validate if the input string contains only Katakana, Hiragana, and Kanji characters. This is helpful for ensuring that the input is valid Japanese text.

### 2. Hyperlink Generation for Jisho.org Search

When valid Japanese text is inputted, the script generates a hyperlink to search the input text on [Jisho.org](https://www.jisho.org/), a comprehensive Japanese dictionary. The generated hyperlink is copied to the clipboard for easy access.

### 3. Sentence Parsing and Hyperlink Generation

If the input contains two sentences separated by `<br><br>`, the script parses each sentence separately and generates hyperlinks for each sentence. Additionally, it provides a hyperlink for translation using Google Translate.

### 4. Hyperlink Generation for Single Sentences

For single sentences that do not match the above pattern, the script generates a hyperlink to search the input text on Jisho.org and provides a translation link using Google Translate.

## How to Use

1. Clone the repository to your local machine.
2. Ensure that PowerShell is installed on your system.
3. Open PowerShell and navigate to the directory containing the script.
4. Run the script by executing `.\JapaneseTextProcessingScript.ps1`.
5. Follow the on-screen instructions to input Japanese text.
6. The script will generate hyperlinks and provide translations based on the input text.

## Note

- Ensure that your input follows the expected patterns to generate accurate hyperlinks and translations.
- The script relies on internet connectivity to fetch data from Jisho.org and Google Translate.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
