class NSAConfig:
    compress_type: str = "weightedpool"
    kernel_size: int = 32
    kernel_stride: int = 16
    block_size: int = 64
    topk: int = 16
    init_blocks: int = 1
    local_blocks: int = 2
    window_size: int = 512