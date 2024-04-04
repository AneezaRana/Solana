import './App.css';
import Comapnies from './components/Companies/Companies';
import Footer from './components/Footer/Footer';
import Header from "./components/Header/Header";
import InfoBar from './components/InfoBar/InfoBar';
import Section1 from './components/Section1/Section1';
import Section2 from './components/Section2/Section2';

function App() {
  return (
    <main className="wrapper">
      <InfoBar />
      <Header />
      <Section1 />
      <Comapnies />
      <Section2 />
      <Footer />
    </main>
  );
}
export default App;
