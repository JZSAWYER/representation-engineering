import pipeline
from repe import repe_pipeline_registry # register 'rep-reading' and 'rep-control' tasks into Hugging Face pipelines
repe_pipeline_registry()

# ... initializing model and tokenizer ....

rep_reading_pipeline =  pipeline("rep-reading", model=model, tokenizer=tokenizer)
rep_control_pipeline =  pipeline("rep-control", model=model, tokenizer=tokenizer, **control_kwargs)