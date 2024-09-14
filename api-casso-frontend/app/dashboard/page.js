// app/layout.tsx
"use client"
import React from 'react';
import styles from './layout.module.css'; // Import CSS module
import  "./boxes.css";
import { useEffect, useState } from 'react';

const Layout = () => {


 

    const [key, setKey] = useState('');
    const [boxes, setBoxes] = useState([]);
    const [data, setData] = useState('');

    const handleKeyChange = (event) => {
        setKey(event.target.value);
    };


    const handleSubmit = () => {
        const newBox = {
            key: key,
            value: { 
                url: '',    
                api: '',
                param: ''
            },
            timestamp: new Date().toISOString() // Optional: add timestamp or other fields if needed
        };
    
        setBoxes(prevBoxes => [newBox, ...prevBoxes]);
        setKey(''); 
        setValue(''); 
    };
    
   

    const handleBlur = async (event, field, index) => {
        const value = event.target.value;

        // Define the updated data based on the field and index
        const updatedData = { [field]: value };
        const boxToUpdate = boxes[index];

        // Prepare the updated box object
        const updatedBox = {
            ...boxToUpdate,
            value: {
                ...boxToUpdate.value,
                ...updatedData
            }
        };

        // Send updated data to the API
        try {
            const response = await fetch('/api/update', { // Ensure this is the correct API route
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ key: updatedBox.key, value: updatedBox.value })
            });

            if (response.ok) {
                console.log('Data updated successfully');
                // Update the local state with the updated box
                setBoxes(prevBoxes => {
                    const newBoxes = [...prevBoxes];
                    newBoxes[index] = updatedBox;
                    return newBoxes;
                });
            } else {
                console.error('Error updating data');
            }
        } catch (error) {
            console.error('Error:', error);
        }
    };
    
    useEffect(() => {
        // Fetch data from the API route
        const fetchData = async () => {
            const response = await fetch('/api/hello?key=hola');
            
            const result = await response.json();
         
            setData(result.value);
        };

        fetchData();
    }, []);


  return (
    <div className={styles.container}>
      <header className={styles.header}>
        <h1>Dashboard</h1>



        <input
        type="text"
     
        className={styles.inputField}
      
      />

   
        <p>
            {data}
        </p>

        <div className="container">
          
            <button onClick={handleSubmit} className="submit-button">Submit</button>
            <div className="boxes-container">
                {boxes.map((box, index) => (
                    <div className="curved-box">
                    {box}
                    <div className='big-container'>
                        <div className='item-container'>
                            <div className='item'>url</div>
                            <input  className='item-input' placeholder='Enter URL' />
                        </div>
                        <div className='item-container'>
                            <div className='item'>api</div>
                            <input className='item-input' placeholder='Enter API' />
                        </div>
                        <div className='item-container'>
                            <div className='item'>param</div>
                            <input className='item-input' placeholder='Enter Param' />
                        </div>
                </div>
               </div>
                ))}
            </div>
        </div>
      </header>
      
      <nav className={styles.sidebar}>
        <ul>
          <li><button onClick={() => handleNavigation('/dashboard')}>Dashboard</button></li>
          <li><button onClick={() => handleNavigation('/profile')}>Profile</button></li>
          <li><button onClick={() => handleNavigation('/settings')}>Settings</button></li>
          <li><button onClick={() => handleNavigation('/reports')}>Reports</button></li>
          <li><button onClick={() => handleNavigation('/help')}>Help</button></li>
        </ul>
      </nav>
      <main className={styles.mainContent}>
         
      </main>
    </div>
  );
};

export default Layout;