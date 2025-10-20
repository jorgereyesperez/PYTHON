class Pokemon
  attr_accessor :nombre, :habilidad, :habilidad_oculta, :egg_moves, :nivel_min, :nivel_max

def initialize(nombre, habilidad, habilidad_oculta, egg_moves, nivel_min, nivel_max)
    @nombre = nombre
    @habilidad = habilidad
    @habilidad_oculta = habilidad_oculta
    @egg_moves = egg_moves
    @nivel_min = nivel_min
    @nivel_max = nivel_max
end

def obtener_nivel
rand(@nivel_min..@nivel_max)  # Nivel aleatorio entre min y max
end

def obtener_habilidad
    # Decide si el Pokémon tiene habilidad oculta
  if rand(2) == 0
      return @habilidad_oculta, "oculta"
  else
      return @habilidad, "normal"
     end
end

def obtener_movimiento_huevo
    # Si el Pokémon tiene movimientos de huevo
  if @egg_moves.any?
    return @egg_moves.sample
  else
    return "Ninguno"
    end
end

RUTA_1 = [
  Pokemon.new("Poochyena", "Run Away", "Rattled", ["Fire Fang", "Ice Fang", "Thunder Fang"], 5, 8),
  Pokemon.new("Zigzagoon", "Pickup", "Quick Feet", ["Extreme Speed", "Charm", "Mud-Slap"], 5, 8),
  Pokemon.new("Wurmple", "Shield Dust", "", [], 5, 8)
]

RUTA_2 = [
  Pokemon.new("Lotad", "Rain Dish", "Own Tempo", ["Synthesis", "Razor Leaf", "Water Gun"], 6, 10),
  Pokemon.new("Seedot", "Chlorophyll", "Pickpocket", ["Leech Seed", "Defog", "Night Slash"], 6, 10),
  Pokemon.new("Ralts", "Synchronize", "Telepathy", ["Knock Off", "Destiny Bond", "Mystical Fire"], 6, 10),
  Pokemon.new("Surskit", "Swift Swim", "Rain Dish", ["Bug Bite", "Hydro Pump", "Aqua Jet"], 6, 10)
]

def mostrar_pokemon_salvaje(localizacion)
  pokemon_lista = Object.const_get(localizacion)  # Se obtiene la constante de la ruta por nombre
  if pokemon_lista
    puts "\nPokémon encontrados en #{localizacion}:"
    pokemon_lista.each_with_index do |pkmn, idx|
      nivel = pkmn.obtener_nivel
      habilidad, tipo_habilidad = pkmn.obtener_habilidad
      movimiento_huevo = pkmn.obtener_movimiento_huevo

      puts "#{idx + 1}. #{pkmn.nombre} (Nivel #{nivel})"
      puts "   Habilidad: #{habilidad} (#{tipo_habilidad})"
      puts "   Movimiento huevo: #{movimiento_huevo}\n"

      # Opción de lucha o captura
      puts "¿Quieres luchar o capturar a #{pkmn.nombre}? (luchar/capturar)"
      accion = gets.chomp.downcase
      if accion == "capturar"
        if intentar_captura(pkmn)
          return  # Captura exitosa, termina el encuentro
        end
      elsif accion == "luchar"
        luchar(pkmn, nivel)  # Luchar contra el Pokémon
      end
    end
  else
    puts "\nLa ruta '#{localizacion}' no está en la base de datos."
  end
end

def intentar_captura(pokemon)
  probabilidad_captura = rand
  if probabilidad_captura < 0.3
    puts "\n¡Felicidades! Has capturado a #{pokemon.nombre}!"
    return true
  else
    puts "\nEl intento de captura falló. El #{pokemon.nombre} escapó."
    return false
  end
end

def luchar(pokemon, nivel)
  puts "\n¡Has comenzado una pelea contra #{pokemon.nombre} de nivel #{nivel}!"
  chance_lucha = rand
  if chance_lucha < 0.5
    puts "\n¡Has ganado la pelea contra #{pokemon.nombre}!"
    return true
  else
    puts "\nHas perdido la batalla contra #{pokemon.nombre}. El Pokémon escapó."
    return false
  end
end
