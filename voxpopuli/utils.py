# Copyright (c) Facebook, Inc. and its affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

from typing import Optional

from parallelbar import progress_map


def multiprocess_run(
        a_list: list, func: callable, n_workers: Optional[int] = None
):
    total = len(a_list)
    if n_workers is None:
        n_workers = 8
    progress_map(func, a_list, n_cpu=n_workers, total=total)
