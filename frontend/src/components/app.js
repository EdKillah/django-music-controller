import React, { Component } from 'react';
import { render } from "react-router-dom";


export default class App extends Component {


    constructor(props) {
        super(props);
    }

    render() {
        return (
            <h1>React app</h1>
        );
    }
}

const appDiv = document.getElementById('app'); 
render(<App />, appDiv);