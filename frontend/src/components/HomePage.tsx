import { FC } from 'react'
import IPage from '../interfaces/IPage';
import PhraseForm from './phrase_form'
import HomePageStyle from './styles/HomePageStyle';
import Navbar from './Navbar';
import MainH1 from './styles/MainH1'

const Proc_Phrase:FC<IPage> = () => {
    return(
        <HomePageStyle>
            <Navbar/>
            <MainH1 value={"<NLP Brasil/>"}/> 
            <PhraseForm/>
        </HomePageStyle>
    )
    
};

export default Proc_Phrase