while getopts p:l: flag
do
    case "${flag}" in
        l) language=${OPTARG};;
        p) problem=${OPTARG};;
    esac
done
echo "Fetching problem: $problem";

problempath="./$language/$problem"
mkdir $problempath
echo "Created $problempath"

curl "https://open.kattis.com/problems/$problem/file/statement/samples.zip" --output "$problempath/$problem.zip"
mkdir "$problempath/samples"
unzip "$problempath/$problem.zip" -d "$problempath/samples"
rm "$problempath/$problem.zip"
 
echo "
$problem
Author: Swopnil Shrestha
Problem: https://open.kattis.com/problems/$problem" > "$problempath/readme.txt"

if [ $language = "rust" ]; then
    echo "Creating rust files"
    touch "$problempath/main.rs"
    echo "Execution: rustc main.rs && ./main < ./samples/<sample>.in" >> "$problempath/readme.txt"
elif [ $language = "python3" ]; then
    echo "Creating python files"
    touch "$problempath/$problem.py"
    echo "Execution: python3 $problem.py < ./samples/<sample>.in" >> "$problempath/readme.txt"
elif [ $language = "java" ]; then
    echo "Creating java files"
    touch "$problempath/$problem.java"
    echo "Execution: javac <problem>.java && java <problem>" >> "$problempath/readme.txt"
fi
