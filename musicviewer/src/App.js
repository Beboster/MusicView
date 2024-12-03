import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
    const [data, setData] = useState(null); // Data from the backend
    const [inputValue, setInputValue] = useState(''); // Artist input
    const [inputValue2, setInputValue2] = useState(''); // Song title input
    const [searchQuery, setSearchQuery] = useState(null); // Search trigger

    // Handle input changes
    const handleChange = (event) => {
        setInputValue(event.target.value); // Update artist input
    };

    const handleChange2 = (event) => {
        setInputValue2(event.target.value); // Update song title input
    };

    const handleSearch = () => {
        // Combine artist and song title into a search query
        const query = { artist: inputValue, song: inputValue2 };
        setSearchQuery(query); // Trigger the search with updated query
    };

    // Fetch data when searchQuery changes
    useEffect(() => {
        if (searchQuery) {
            axios.get('http://127.0.0.1:5000/api/data', { params: searchQuery })
                .then(response => {
                    setData(response.data); // Update data state with the result
                })
                .catch(error => {
                    console.error('Error fetching data:', error);
                });
        }
    }, [searchQuery]); // Only re-run when searchQuery changes

    // Send data via POST request
    const sendData = () => {
        axios.post('http://127.0.0.1:5000/api/data', { 
            textInput: inputValue, 
            textInput2: inputValue2 
        })
        .then(response => {
            console.log('Response:', response.data);
        })
        .catch(error => {
            console.error('Error sending data:', error);
        });
    };

    return (
        <div>
            <h1>React and Python Integration</h1>

            <h2>Search for Data</h2>
            <input 
                type="text" 
                value={inputValue} 
                onChange={handleChange} 
                placeholder="Artist" 
            />
            <input 
                type="text" 
                value={inputValue2} 
                onChange={handleChange2} 
                placeholder="Song Title" 
            />
            <button onClick={handleSearch}>Search</button>

            <h2>Send Data to Python</h2>
            <button onClick={sendData}>Send Data</button>

            <h3>Search Results</h3>
            {data ? (
                <pre>{JSON.stringify(data, null, 2)}</pre>
            ) : (
                <p>No results yet. Try a search!</p>
            )}

            <p>Artist Chosen: {inputValue}</p>
            <p>Song Chosen: {inputValue2}</p>
        </div>
    );
}

export default App;
