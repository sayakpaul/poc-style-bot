import torch
from diffusers import HunyuanVideoPipeline, HunyuanVideoTransformer3DModel
from diffusers.utils import export_to_video

model_id = "tencent/HunyuanVideo"
transformer = HunyuanVideoTransformer3DModel.from_pretrained(model_id, subfolder="transformer", torch_dtype=torch.bfloat16, revision="refs/pr/18")
pipe = HunyuanVideoPipeline.from_pretrained(model_id, transformer=transformer, torch_dtype=torch.float16, revision="refs/pr/18")
pipe.vae.enable_tiling()
pipe.to("cuda")

output = pipe(
    prompt="A cat walks on the grass, realistic",
    height=320,
    width=512,
    num_frames=61,
    num_inference_steps=30,
).frames[0]
export_to_video(output, "output_hunyuan.mp4", fps=15)