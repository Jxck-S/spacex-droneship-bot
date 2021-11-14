import React from 'react'
import { GoogleMap, useJsApiLoader } from '@react-google-maps/api';
import { Typography } from '@mui/material';


const containerStyle = {
  width: '700px',
  height: '700px'
};

function MapDisplay(props) {
  const { isLoaded } = useJsApiLoader({
    id: 'google-map-script',
    googleMapsApiKey: ""
  })

  // Coordinates
  let someLat = parseFloat(props.latCord);
  let someLon = parseFloat(props.lonCord);

  const newCenter = {
    lat: someLat,
    lng: someLon
  };

  const [map, setMap] = React.useState(null);

  const onLoad = React.useCallback(function callback(map) {
    const bounds = new window.google.maps.LatLngBounds();
    map.fitBounds(bounds);
    setMap(map)
  }, [])

  const onUnmount = React.useCallback(function callback(map) {
    setMap(null)
  }, [])


  return isLoaded ? (
    <>
      <Typography sx={{fontSize: "2rem", color:"#fff"}}>Ship Name: {props.shipName}</Typography>
      <Typography sx={{fontSize: "1rem", color:'#fff'}}>Latitude: {props.latCord} Longitude: {props.lonCord}</Typography>

      <GoogleMap
        mapContainerStyle={containerStyle}
        center={newCenter}
        zoom={1}
        onLoad={onLoad}
        onUnmount={onUnmount}
      >
        <></>
      </GoogleMap>


      </>
  ) : <>
  </>
}

export default React.memo(MapDisplay)