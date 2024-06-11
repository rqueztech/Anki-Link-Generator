
# Function to check if the string contains only Katakana, Hiragana, and Kanji
function ContainsOnlyJapaneseCharacters {
    param (
        [string]$str
    )
    # Katakana, Hiragana, and Kanji Unicode ranges
    $japaneseCharPattern = '^[\p{IsKatakana}\p{IsHiragana}\p{IsCJKUnifiedIdeographs}]+$'
    return $str -match $japaneseCharPattern
}

while(1) {

    $newinput = Read-Host "Your input here"

    if (ContainsOnlyJapaneseCharacters $newinput) {
        $newstring = "<a href = `"https://www.jisho.org/search/" + $newinput + "`" " + "style=`"text-decoration: none;`">$newinput</a>"

        set-clipboard $newstring
        $newstring
    }

    elseif ($newinput -match "<br><br>") {
    
    # Regular expression pattern to match the first and second sentences
    $regex = "^(.*?)<br><br>(.*?)"

    # Replacement pattern to wrap sentences in <a> tags
    $replacement = '<a href="https://www.jisho.org/search/$1" style="text-decoration: none;">$1</a><br><a href="https://translate.google.co.jp/?hl=en&sl=ja&tl=en&text=$1" style="text-decoration: none;">Translation</a><br><br><a href="https://www.jisho.org/search/$2" style="text-decoration: none;">$2</a><a href="https://translate.google.co.jp/?hl=en&sl=ja&tl=en&text=$2" style="text-decoration: none;"><br>Translation</a>'

    # Applying the regex substitution
    $result = [regex]::Replace($newinput, $regex, $replacement)

    # Output the result
    $result

    set-clipboard $result

    $result
    }

    else {
        $prelinkk = "`"https://www.jisho.org/search/$newinput`""
        
        $linkopen = "<a href = "
        $linkclose = " style = `"text-decoration: none;`">"
        $wholelinkclose ="</a>"

        $newstring = $linkopen + $prelinkk + $linkclose  + $newinput + $wholelinkclose
        
        $newstring = $newstring + "<br><a href = `"https://translate.google.co.jp/?hl=en&sl=ja&tl=en&text=" + $newinput + "`">Translation</a>"

        $newstring
        
        set-clipboard $newstring
    }
}

