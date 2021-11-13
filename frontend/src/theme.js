import {createTheme} from '@mui/material'

const theme = createTheme({
    palette: {
        primary: {
            main: '#fff',
            contrastText: '#000'
        },
        secondary: {
            main: '#FFEE16',
            contrastText: '#000'
        },
        text: {
            primary: "#fff"
        }
    },
    typography: {
        h1: {
            fontSize: '3rem',
            fontWeight: '600'
        },
        h2: {
            fontSize: '2.5rem',
            fontWeight: '400'
        },
        h3: {
            fontSize: '2rem'
        },
        h4: {
            fontSize: '1.5rem'
        }
    },
    // shape: {
    //     borderRadius: 0
    // }
});

export default theme