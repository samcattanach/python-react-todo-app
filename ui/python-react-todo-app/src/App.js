import logo from './logo.svg';
import './App.css';
import React from 'react';
import TodoList from './components/TodoApp';

function App() {
    return ( 
        <div className = "App" >
            <TodoList/>
        </div>
    );
}

export default App;