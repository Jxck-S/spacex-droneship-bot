import React, { useState } from 'react';
import {ThemeProvider} from '@mui/material'
import theme from './theme'
import Navbar from './components/Navbar'
import MyComponent from './components/MyComponent';
import { GoogleMap, useJsApiLoader } from '@react-google-maps/api';
import {
  Box,
  // AppBar,
  // Toolbar,
  Button,
  Typography,
  // IconButton
} from '@mui/material'

const App = () =>
{

  // const count = 0;
  // const url = "http://gcp.jackstech.net/asog.json"

  // const fetchData = () => {
  // fetch(url).then(response => response.json()).then(data => console.log(data))

  
  const [aCoordinate, getFetchData] = useState('');


  // https://foodish-api.herokuapp.com/api/
  async function fetchData() {
    try {
      let response = await fetch('https://asogflask.herokuapp.com/asog.json', {mode: 'no-cors'});
      let responseJson = await response.json();

      let coordinates = responseJson["LENGTH"];
      // console.log(coordinates.text);
      
      getFetchData(coordinates);
      // console.log(responseJson.image);
      // console.log("coordinates = " + coordinatesPrint);

     } catch(error) {
      console.error(error);
    }
  }


  return (
      <ThemeProvider theme={theme}>
        <Navbar />

        <Box sx={{display:"flex", flexDirection: "column", justifyContent:"center", alignItems:"center"}}>
          <Button variant="contained" onClick={fetchData}>Fetch some Data</Button>

          <Typography sx={{fontSize: "2rem", color:"#fff"}}>Data received: {aCoordinate}</Typography>
          <MyComponent />
        </Box>
        
      </ThemeProvider>
  );
}

export default App;
