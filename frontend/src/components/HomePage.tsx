import { FC } from 'react'
import IPage from '../interfaces/IPage';
import PhraseForm from './phrase_form'
import HomePageStyle from './styles/HomePageStyle';
import Navbar from './Navbar';

const Proc_Phrase:FC<IPage> = () => {
    return(
        <HomePageStyle>
            <Navbar/>
            <PhraseForm/>
        </HomePageStyle>
    )
    
};

export default Proc_Phrase