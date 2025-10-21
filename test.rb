Registro_Pokemon = {}

NATURALEZAS = {
  "Hardy"   => [nil, nil],
  "Lonely"  => ["Ataque", "Defensa"],
  "Brave"   => ["Ataque", "Velocidad"],
  "Adamant" => ["Ataque", "Ataque Especial"],
  "Naughty" => ["Ataque", "Defensa Especial"],

  "Bold"    => ["Defensa", "Ataque"],
  "Docile"  => [nil, nil],
  "Relaxed" => ["Defensa", "Velocidad"],
  "Impish"  => ["Defensa", "Ataque Especial"],
  "Lax"     => ["Defensa", "Defensa Especial"],

  "Timid"   => ["Velocidad", "Ataque"],
  "Hasty"   => ["Velocidad", "Defensa"],
  "Serious" => [nil, nil],
  "Jolly"   => ["Velocidad", "Ataque Especial"],
  "Naive"   => ["Velocidad", "Defensa Especial"],

  "Modest"  => ["Ataque Especial", "Ataque"],
  "Mild"    => ["Ataque Especial", "Defensa"],
  "Quiet"   => ["Ataque Especial", "Velocidad"],
  "Bashful" => [nil, nil],
  "Rash"    => ["Ataque Especial", "Defensa Especial"],

  "Calm"    => ["Defensa Especial", "Ataque"],
  "Gentle"  => ["Defensa Especial", "Defensa"],
  "Sassy"   => ["Defensa Especial", "Velocidad"],
  "Careful" => ["Defensa Especial", "Ataque Especial"],
  "Quirky"  => [nil, nil]
}

#===============================================================================
# Clase Pokémon personalizada
#===============================================================================
class PokemonDexnav
  attr_accessor :nombre, :habilidad, :habilidad_oculta, :egg_moves,
                :nivel_min, :nivel_max, :es_shiny, :IVs, :naturaleza, :stats_base

  def initialize(nombre, habilidad, habilidad_oculta, egg_moves, nivel_min, nivel_max,
                 hp_base, atk_base, def_base, sp_atk_base, sp_def_base, vel_base)
    @nombre = nombre
    @habilidad = habilidad
    @habilidad_oculta = habilidad_oculta
    @egg_moves = egg_moves
    @nivel_min = nivel_min
    @nivel_max = nivel_max
    @es_shiny = false

    @stats_base = {
      "HP" => hp_base,
      "Ataque" => atk_base,
      "Defensa" => def_base,
      "Ataque Especial" => sp_atk_base,
      "Defensa Especial" => sp_def_base,
      "Velocidad" => vel_base
    }

    @IVs = generar_ivs
    @naturaleza = obtener_naturaleza
  end

  def determinar_shiny
    @es_shiny = rand < 1.0 / 512
  end

  def obtener_nivel
    rand(@nivel_min..@nivel_max)
  end

  def obtener_habilidad
    if [true, false].sample
      [@habilidad_oculta, "oculta"]
    else
      [@habilidad, "normal"]
    end
  end

  def obtener_movimiento_huevo
    return "Ninguno" if @egg_moves.empty?
    @egg_moves.sample
  end

  def generar_ivs
    ivs = {}
    @stats_base.keys.each { |stat| ivs[stat] = rand(0..31) }
    ivs
  end

  def obtener_naturaleza
    NATURALEZAS.keys.sample
  end

  def calcular_estadisticas_reales(nivel)
    stats_reales = {}
    plus_stat, minus_stat = NATURALEZAS[@naturaleza]

    @stats_base.each do |stat, base|
      iv = @IVs[stat]
      if stat == "HP"
        real = (((2 * base + iv) * nivel / 100.0) + nivel + 10).to_i
      else
        mod = 1.0
        mod = 1.1 if stat == plus_stat
        mod = 0.9 if stat == minus_stat
        real = ((((2 * base + iv) * nivel / 100.0) + 5) * mod).to_i
      end
      stats_reales[stat] = real
    end

    stats_reales
  end
end

#===============================================================================
# Base de datos de Pokémon por ruta
#===============================================================================
Dexnav_Data = {
  "Ruta 1" => [
    PokemonDexnav.new("Poochyena", "Run Away", "Rattled", ["Fire Fang", "Ice Fang", "Thunder Fang"], 5, 8, 35, 55, 35, 30, 30, 35),
    PokemonDexnav.new("Zigzagoon", "Pickup", "Quick Feet", ["Extreme Speed", "Charm", "Mud-Slap"], 5, 8, 38, 30, 41, 30, 41, 60),
    PokemonDexnav.new("Wurmple", "Shield Dust", "", [], 5, 8, 45, 45, 35, 20, 30, 20)
  ],
  "Ruta 2" => [
    PokemonDexnav.new("Lotad", "Rain Dish", "Own Tempo", ["Synthesis", "Razor Leaf", "Water Gun"], 9, 12, 40, 30, 30, 40, 50, 30),
    PokemonDexnav.new("Seedot", "Chlorophyll", "Pickpocket", ["Leech Seed", "Defog", "Night Slash"], 9, 12, 40, 40, 50, 30, 30, 30),
    PokemonDexnav.new("Ralts", "Synchronize", "Telepathy", ["Knock Off", "Destiny Bond", "Mystical Fire"], 9, 12, 28, 25, 25, 45, 35, 40),
    PokemonDexnav.new("Surskit", "Swift Swim", "Rain Dish", ["Bug Bite", "Hydro Pump", "Aqua Jet"], 9, 12, 40, 30, 32, 50, 52, 65)
  ]
}

#===============================================================================
# Funciones principales
#===============================================================================
def registrar_pokemon(localizacion, pokemon, habilidad, movimiento_huevo, naturaleza)
  Registro_Pokemon[localizacion] ||= {}
  unless Registro_Pokemon[localizacion].key?(pokemon.nombre)
    Registro_Pokemon[localizacion][pokemon.nombre] = {
      "Habilidad" => habilidad,
      "Movimiento huevo" => movimiento_huevo,
      "Naturaleza" => naturaleza
    }
    puts " #{pokemon.nombre} ha sido registrado en la DexNav de #{localizacion}."
  end
end

def mostrar_pokemon_salvaje(localizacion)
  lista = Dexnav_Data[localizacion]
  if lista
    puts "\nPokémon encontrados en #{localizacion}:\n\n"
    lista.each_with_index do |pkmn, i|
      pkmn.determinar_shiny
      nivel = pkmn.obtener_nivel
      habilidad, tipo_habilidad = pkmn.obtener_habilidad
      mov_huevo = pkmn.obtener_movimiento_huevo
      stats = pkmn.calcular_estadisticas_reales(nivel)
      registrar_pokemon(localizacion, pkmn, habilidad, mov_huevo, pkmn.naturaleza)

      iconos = ""
      iconos += " ⭐" if pkmn.es_shiny
      iconos += " 🕶️" if tipo_habilidad == "oculta"

      puts "#{i + 1}. #{pkmn.nombre}#{iconos} (Nivel #{nivel})"
      puts "   Habilidad: #{habilidad} (#{tipo_habilidad})"
      puts "   Movimiento huevo: #{mov_huevo}"
      puts "   Naturaleza: #{pkmn.naturaleza}"
      puts "   IVs:"
      pkmn.IVs.each { |stat, iv| puts "     - #{stat}: #{iv}" }
      puts "   Estadísticas reales:"
      stats.each { |stat, val| puts "     - #{stat}: #{val}" }
      puts
    end

    print "Elige el número del Pokémon al que quieres enfrentarte (1-#{lista.length}): "
    sel = gets.to_i
    pkmn = lista[sel - 1]
    return unless pkmn

    print "¿Quieres luchar o capturar a #{pkmn.nombre}? (luchar/capturar): "
    accion = gets.strip.downcase

    if accion == "capturar"
      intentar_captura(pkmn)
    elsif accion == "luchar"
      luchar(pkmn, pkmn.obtener_nivel)
    else
      puts "Opción inválida."
    end
  else
    puts "\nLa ruta '#{localizacion}' no está disponible."
  end
end

def mostrar_registro
  if Registro_Pokemon.empty?
    puts "\n📭 No has registrado ningún Pokémon aún."
    return
  end
  puts "\n📗 REGISTRO DEXNAV:"
  Registro_Pokemon.each do |ruta, pokes|
    puts "\n📍 #{ruta}:"
    pokes.each do |nombre, datos|
      puts " - #{nombre}"
      puts "   Habilidad: #{datos['Habilidad']}"
      puts "   Movimiento huevo: #{datos['Movimiento huevo']}"
      puts "   Naturaleza: #{datos['Naturaleza']}"
    end
  end
end

def intentar_captura(pokemon)
  if rand < 0.3
    puts "\n¡Felicidades! Has capturado un #{pokemon.nombre}!"
    true
  else
    puts "\nEl intento de captura falló. El #{pokemon.nombre} escapó."
    false
  end
end

def luchar(pokemon, nivel)
  puts "\n¡Has comenzado una pelea con un #{pokemon.nombre} de nivel #{nivel}!"
  if rand < 0.5
    puts "\n¡Has ganado la pelea contra #{pokemon.nombre}!"
    true
  else
    puts "\nHas perdido la pelea contra #{pokemon.nombre}... El Pokémon escapó."
    false
  end
end

def explorar_ruta
  puts "=== DEXNAV BÁSICO ==="
  puts "Rutas disponibles:"
  Dexnav_Data.keys.each { |r| puts " - #{r}" }

  loop do
    puts "\nOpciones:"
    puts " - Escribe el nombre exacto de la ruta para explorar."
    puts " - Escribe 'registro' para ver tu Pokédex registrada."
    puts " - Escribe 'salir' para volver al menú principal."
    print "\n¿Qué quieres hacer?: "
    opcion = gets.strip.capitalize

    case opcion.downcase
    when "salir"
      puts "Volviendo al menú principal."
      break
    when "registro"
      mostrar_registro
    else
      if Dexnav_Data.key?(opcion)
        mostrar_pokemon_salvaje(opcion)
      else
        puts "\nLa ruta '#{opcion}' no está disponible."
      end
    end
  end
end

#===============================================================================
# Ejecutar script manualmente fuera de Essentials
#===============================================================================
if __FILE__ == $0
  explorar_ruta
end