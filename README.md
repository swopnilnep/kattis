# Kattis

Some of the problems I have solved on Kattis. 

The directory names correspond to `problemID` on Kattis. Most of the problems solved currently are on `python3`, however I plan to use Kattis to learn and implement solutions in other languages as I go.

In order to dynamically generate readme and templates for each problem, I am using [fetch.sh](./fetch.sh). It takes a language and problem as an argument and generates files for each problem.

## Execution 

For Python3: 
```zsh
cd python3/<problem>
python <problem>.py < samples/<sample>.in
```

For Rust: 
```zsh
cd rust/<problem>
rustc main.rs && ./main < samples/<sample>.in
```

For Java: 
```zsh
cd java/<problem>
javac <problem>.java && java ./<problem> < samples/<sample>.in
```

## License

All code is provided under the MIT license.
https://mit-license.org/
