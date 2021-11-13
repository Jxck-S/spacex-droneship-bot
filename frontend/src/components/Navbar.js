import React from 'react'
// import App from '../App'

import {
    // Box,
    AppBar,
    Toolbar,
    Button,
    Typography
} from '@mui/material'


const Navbar = () => {
    return (
        <>
            <AppBar sx={{bgcolor: "secondary.main", borderRadius: '0  0 .5rem .5rem'}}>
                <Toolbar>
                    <Typography color="#333">SpaxeX Droneship Bot Dashboard</Typography>
                    <Button variant="contained">Test Button</Button>
                </Toolbar>
            </AppBar>
        </>
    )
}

export default Navbar
