import React from 'react'
// import App from '../App'
import GitHubIcon from '@mui/icons-material/GitHub';
import DirectionsBoatIcon from '@mui/icons-material/DirectionsBoat';

import {
    Box,
    AppBar,
    Toolbar,
    // Button,
    Typography,
    IconButton
} from '@mui/material'


const Navbar = () => {
    return (
        <Box sx = {{mx: '5rem'}}>
            <AppBar position="relative" sx={{bgcolor: "secondary.main", borderRadius: '0  0 .5rem .5rem', margin: '0 1rem'}}>
                <Toolbar sx={{display:'flex', justifyContent:'space-between'}}>
                    <IconButton color="primary" href="/"><DirectionsBoatIcon /></IconButton>
                    <Typography sx={{fontWeight: 800}} color="#333">SpaxeX Droneship Bot</Typography>
                    <IconButton color="primary" href="https://github.com/Jxck-S/spacex-droneship-bot"><GitHubIcon /></IconButton>
                </Toolbar>
            </AppBar>
        </Box>
    )
}

export default Navbar
