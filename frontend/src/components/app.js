import React, { Component } from 'react';
import { render }  from "react-dom";
import HomePage from './HomePage';


export default class App extends Component {


    constructor(props) {
        super(props);
    }

    render() {
        return (
            <>
                <h1>{this.props.name}</h1>
                <HomePage />
            </>
        );
    }
}

const appDiv = document.getElementById('app'); 
console.log("AppDiv: ",appDiv);
render(<App name="Eduard" />, appDiv);