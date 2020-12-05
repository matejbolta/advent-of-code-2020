(* Uporaba knjižnjice Str na WINDOWSU:
http://pleac.sourceforge.net/pleac_ocaml/patternmatching.html *)
# load "str.cma";;

let day = "4"

let fields = ["byr"; "iyr"; "eyr"; "hgt"; "hcl"; "ecl"; "pid"; "cid"]

(* Note to self: https://stackoverflow.com/questions/39813584/ *)
let fix_passport_whitespace list = (* ["ecl:utc byr:2029"] -> ["ecl:utc"; "byr:2029"] *)
  let rec aux acc = function
    | [] -> acc
    | str :: strs -> (* String.contains : string -> char -> bool *)
      if String.contains str ' ' then aux (String.split_on_char ' ' str @ acc) strs
      else aux (str :: acc) strs
  in
  aux [] list
;;

(* Slovarje bom predstavil kot (key * value) list *)
(* oziroma (string * string) list, ker ne bom definiral novega tipa *)
let list_to_dict list = (* list predstavlja passport *)
  let get_key element = String.sub element 0 3 in
  let get_value element = String.sub element 4 (String.length element - 4) in
  let rec aux acc = function
    | [] -> acc
    | pass :: passes -> aux ((get_key pass, get_value pass) :: acc) passes
  in
  aux [] list
;;

let rec valid_passport1 check fields pass =
    let keys = List.map fst pass in
    match fields with
    | [] -> check
    | field :: tail -> (* List.exists : ('a -> bool) -> 'a list -> bool *)
      if (not (List.exists ((=) field) keys)) && (field <> "cid") then false
      else valid_passport1 check tail pass
;;

let count_valid_1 list = (* (string * 'a) list list -> int *)
  let rec count_aux counter = function
  | [] -> counter
  | pass :: passes ->
    if (valid_passport1 true fields pass) then count_aux (counter + 1) passes
    else count_aux counter passes
  in
  count_aux 0 list
;;

let rec get field pass = (* get : 'a -> ('a * 'b) list -> 'b *)
  match pass with
  | [] -> failwith "line cca 53"
  | (k, v) :: tail when k = field -> v
  | _ :: tail -> get field tail
;;

let is_digit string = (* https://stackoverflow.com/questions/43554262/ *)
  try int_of_string string |> ignore; true
  with Failure _ -> false
;;

let between x min max = (min <= x) && (x <= max)

let valid_hgt v =
  if (String.sub v (String.length v - 2) 2) = "cm"
    &&
    between (int_of_string (String.sub v 0 (String.index v 'c'))) 150 193
    then true

  else if (String.sub v (String.length v - 2) 2) = "in"
    &&
    between (int_of_string (String.sub v 0 (String.index v 'i'))) 59 76
    then true
  else false
;;

let valid_hcl v =
  if v.[0] <> '#' then false
  else
    let v = Str.split (Str.regexp "") (String.sub v 1 (String.length v - 1)) in (* Odrežemo ničti element, split *)
    let rec valid = function
    | [] -> true
    | x :: xs ->
      if not (List.exists ((=) x) ["0";"1";"2";"3";"4";"5";"6";"7";"8";"9";"a";"b";"c";"d";"e";"f"]) then false
      else valid xs
    in
    valid v
;;

let rec valid_passport2 check fields pass =
  match fields with
    | [] -> check
    | field :: tail ->
      if field = "byr" && (not (1920 <= int_of_string (get field pass) && int_of_string(get field pass) <= 2002)) then false
      else if field = "iyr" && (not (2010 <= int_of_string (get field pass) &&int_of_string (get field pass) <= 2020)) then false
      else if field = "eyr" && (not (2020 <= int_of_string (get field pass) &&int_of_string (get field pass) <= 2030)) then false
      else if field = "hgt" && (not (valid_hgt (get field pass))) then false
      else if field = "hcl" && (not (valid_hcl (get field pass))) then false
      else if field = "ecl" && (not (List.exists ((=) (get field pass)) ["amb"; "blu";"brn"; "gry"; "grn"; "hzl"; "oth"])) then false
      else if field = "pid" && (String.length (get field pass) <> 9 || not (is_digit (get field pass))) then false
      else valid_passport2 check tail pass
;;

let count_valid_2 list = (* (string * 'a) list list -> int *)
  let rec count_aux counter = function
    | [] -> counter
    | pass :: passes ->
      if (valid_passport1 true fields pass && valid_passport2 true fields pass)
        then count_aux (counter + 1) passes
      else count_aux counter passes
  in
  count_aux 0 list
;;

let naloga1 vsebina_datoteke =
  let s = vsebina_datoteke
    |> String.trim
    (* Razdelimo na nize s passporti: *)
    |> Str.split (Str.regexp "\n\n") (* https://ocaml.org/manual/libref/Str.html *)
    (* Vsak passport spravimo v obliko seznama *)
    |> List.map (String.split_on_char '\n')
    |> List.map fix_passport_whitespace
    (* Naredimo slovar iz passporta *)
    |> List.map list_to_dict
    (* Preštejemo ustrezne slovarje (=passporte) *)
    |> count_valid_1
    |> string_of_int
  in
  print_endline ("day " ^ day ^ ", puzzle 1: " ^ s);
  s
;;

let naloga2 vsebina_datoteke =
  let s = vsebina_datoteke
    |> String.trim
    |> Str.split (Str.regexp "\n\n")
    |> List.map (String.split_on_char '\n')
    |> List.map fix_passport_whitespace
    |> List.map list_to_dict
    |> count_valid_2
    |> string_of_int
  in
  print_endline ("day " ^ day ^ ", puzzle 2: " ^ s);
  s
;;

let _ =
  let preberi_datoteko ime_datoteke =
    let chan = open_in ime_datoteke in
    let vsebina = really_input_string chan (in_channel_length chan) in
    close_in chan;
    vsebina
  and izpisi_datoteko ime_datoteke vsebina =
    let chan = open_out ime_datoteke in
    output_string chan vsebina;
    close_out chan
  in

  let vsebina_datoteke = preberi_datoteko ("data/day_" ^ day ^ ".in") in
  let odgovor1 = naloga1 vsebina_datoteke
  and odgovor2 = naloga2 vsebina_datoteke
  in

  izpisi_datoteko ("out/day_" ^ day ^ "_1.out") odgovor1;
  izpisi_datoteko ("out/day_" ^ day ^ "_2.out") odgovor2
;;