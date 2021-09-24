import { useRef, useState } from 'react'
import { SubmitHandler, FormHandles } from '@unform/core'
import Input from './input'
import api from './Axios_Conf'
import Drop from './Dropdown'
import IForm from '../interfaces/IFormPhrase'
import IPhrase from '../interfaces/IPhrase'
import PhraseFormStyle from './styles/PhraseFormStyle'

function ReportError(props:any){
	return(
		<p><a href={`/stack/review/${props.phrase}`}>Algo errado?</a></p>
	);
}

function Show(props:any){
	let isHidden = props.isHidden
	const phrase:IPhrase = props.phrase
	if (isHidden) {
		return(
			<>
				<Drop
					
					Polaridade={phrase?.Polaridade}
					Confianca ={phrase?.Confianca}
					NumeroPalavras ={phrase?.NumeroPalavras}
					PalavrasCon = {phrase?.PalavrasCon}
					PalavrasDesc ={phrase?.PalavrasDesc}
					Mensagem={phrase?.Mensagem}
						
									
				/>
				<ReportError phrase={phrase?.Frase}/>
			</>
		)
	}
	return(
		<></>
	)
};

export default function MyForm() {
	const [phrase, setPhrase] = useState<IPhrase>()
	const [hidden, setHidden] = useState(false)
	const formRef = useRef<FormHandles>(null)
	const handleSubmit: SubmitHandler<IForm> = data => {
		api.post(
			'/processing',
			data
		).then((Response) => {
		
			setPhrase(Response.data.data);
		
		})
	}
	
	return(
		<>
			<div className="form">
				<PhraseFormStyle ref={formRef} onSubmit={handleSubmit}>
					<Input name="phrase" placeholder="Frase"/>
					<button type="submit" onClick={() => setHidden(!hidden)}>Enviar!</button>
				</PhraseFormStyle>
			</div>
			<div className="phrase">
				{phrase?.Mensagem} 
			</div>	
			<div className="statics">
				<Show isHidden={hidden} phrase={phrase}/>
				
			</div>
		</>
	);
}