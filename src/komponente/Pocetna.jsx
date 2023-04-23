import {useNavigate} from "react-router-dom";


function Pocetna(){
const navigate=useNavigate();
    return(
    <div  className='pocetna'>
    <div className="hero-text">
        <h1  className="naslov"> Welcome to the world of agriculture!</h1>
    </div>
    
    <br /><br /><br /><br /><br />
    <div>
        <p className="paragraf">Create your own garden and take care of your vegetables with our organic vegetable parameter monitoring system to ensure the best quality vegetables for you and your customers.</p>
    <button  className="btn" onClick={()=>navigate('/makegarden')}>Make your own garden!</button>
    </div>
    
    </div>
  
    
    );
    }
    
    export default Pocetna;
    