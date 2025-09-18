# -*- coding: utf-8 -*-

import json
from pathlib import Path

dir_here = Path(__file__).absolute().parent
path_list_threads_results = dir_here / "list_threads_results.json"
path_list_messages_results = dir_here / "list_messages_results.json"
path_get_thread_result = dir_here / "get_thread_result.json"
path_get_message_result = dir_here / "get_message_result.json"


def write(path: Path, data: dict):
    return path.write_text(json.dumps(data, indent=4, ensure_ascii=False))
