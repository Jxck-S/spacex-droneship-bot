import React, { useState } from 'react';
import {ThemeProvider} from '@mui/material'
import theme from './theme'
import Navbar from './components/Navbar'

import { GoogleMap, useJsApiLoader } from '@react-google-maps/api';

import {
  Box,
  Button,
} from '@mui/material'
import MapDisplay from './components/MapDisplay';

const App = () =>
{  
  const [aCoordinate, getFetchData] = useState('');


  const Input = () => {
    return <MapDisplay latCord={latCords} lonCord={lonCords} shipName={shipName}/>;
  };

  const [googleMapList, setgoogleMapList] = useState([]);

  const onAddBtnClick = event => {
    setgoogleMapList(googleMapList.concat(<Input key={googleMapList.length} />));
  };

  let shipName = undefined;
  let latCords = undefined;
  let lonCords = undefined;

  async function fetchData() {
    try {
      // Fetching JSON data from API
      let response = await fetch('https://asogflask.herokuapp.com/asog.json');
      let responseJson = await response.json();

      // Getting information from fetched data
      shipName = responseJson["SHIPNAME"];
      latCords = responseJson["LAT"];
      lonCords = responseJson["LON"];

      latCords = parseFloat(latCords);
      lonCords = parseFloat(lonCords);
      
      
      onAddBtnClick(); 
      getFetchData(shipName);
           
     } catch(error) {
      console.error(error);
    }
  }

  return (
      <ThemeProvider theme={theme}>
        <Navbar />

        <Box sx={{display:"flex", flexDirection: "column", justifyContent:"center", alignItems:"center"}}>
          <Button sx={{mt: '1rem'}}variant="contained" onClick={fetchData}>Update Data</Button>
          {googleMapList}
        </Box>
        
      </ThemeProvider>
  );
}

export default App;
