'use strict';
console.log('hello fatima');

function Hello(props) {

    // with jsx and Babel
    return (<h1> Hello from react with jsx</h1>);

    // without Babel and jsx
    // return React.createElement('h1', null, 'Hello world (from React)');
}
ReactDOM.render(
    React.createElement(Hello), //here we can do <Hello />,
    document.getElementById('reactGo'),
);