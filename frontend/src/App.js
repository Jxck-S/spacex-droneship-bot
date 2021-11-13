import {ThemeProvider} from '@mui/material'
import theme from './theme'
import Navbar from './components/Navbar'

const App = () =>
{
  return (
      <ThemeProvider theme={theme}>
        <Navbar />
      </ThemeProvider>
  );
}

export default App;
