function wordsUppercase(string) {
    let result = string.toUpperCase()
        .split(/[\W]+/)
        .filter(w => w.length > 0)
        .join(", ");

    console.log(result);
}

wordsUppercase('hello');
wordsUppercase('Hi, how are you?');