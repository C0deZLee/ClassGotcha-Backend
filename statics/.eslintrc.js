module.exports = {
    root: true,
    parser: 'babel-eslint',
    parserOptions: {
        sourceType: 'module'
    },
    // https://github.com/feross/standard/blob/master/RULES.md#javascript-standard-style
    extends: 'standard',
    // required to lint *.vue files
    plugins: [
        'html'
    ],
    // add your custom rules here
    'rules': {
        // no indent errors
        // allow paren-less arrow functions
        'arrow-parens': 0,
        // allow async-await
        'generator-star-spacing': 0,
        // allow debugger during development
        'no-debugger': process.env.NODE_ENV === 'production' ? 2 : 0,
        // shut the fuck up
        'space-before-function-paren': 0,
        'indent': 0,
        'no-multiple-empty-lines': 0,
        'comma-dangle': 0,
        'operator-linebreak': 0,
        'curly': 0,
        'padded-blocks': 0,
        'quotes': 0,
        'no-trailing-spaces': 0,
        'camelcase': 0,
        'no-extend-native': 0,
        'brace-style': 0
    }
}
