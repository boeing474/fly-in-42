# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pboeing- <pboeing-@student.42rio.com>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/10/11 18:21:20 by pboeing-          #+#    #+#              #
#    Updated: 2026/10/11 18:21:20 by pboeing-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
from pathlib import Path

from parsing.map_parser import MapParser
from algorithm.dijkstra import Algorithm
from algorithm.path_checker import PathChecker

def main():
    # 1. Verifica se a Moulinette passou o mapa como argumento
    if len(sys.argv) != 2:
        print("Error: Invalid number of arguments.")
        sys.exit(1)

    map_path = Path(sys.argv[1])

    # 2. Verifica se o arquivo existe
    if not map_path.exists() or not map_path.is_file():
        print(f"Error: File '{map_path}' not found.")
        sys.exit(1)

    try:
        # 3. Faz o parsing do mapa
        level_load = MapParser(map_path).parse_maps()

        # 4. Checa se o caminho é possível
        if not PathChecker(level_load).is_path_possible():
            print("Error: No possible path between start_hub and end_hub")
            sys.exit(1)

        # 5. Roda o algoritmo
        level_algo = Algorithm(level_load).make_algo()
        
        # O algoritmo calculará as rotas. 
        # A impressão dos turnos (ex: D0-Z1 D1-Z2) deve acontecer ou dentro
        # da função make_algo() lá no dijkstra.py, ou você deve imprimir
        # a resposta retornada por level_algo aqui neste ponto.

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
