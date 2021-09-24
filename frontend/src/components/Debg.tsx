import { useRef, useState } from 'react'
import { SubmitHandler, FormHandles } from '@unform/core'
import { Form } from '@unform/web'
import Input from './input'

export default function MyForm() {
	const [phrase, setPhrase] = useState()
	const formRef = useRef<FormHandles>(null)
	const handleSubmit: SubmitHandler = data => {
		setPhrase(data.test)
	}
	
	return(
		<>  
            <Form onSubmit={handleSubmit} ref={formRef}>
                <Input name="test" placeholder="escreve qqr coisa"/>
                <button type="submit">Enviar</button>
            </Form>
            {phrase}
		</>
	);
}