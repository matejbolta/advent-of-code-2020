# load "str.cma";;
let day = "7"


let splitaj = function
  | color :: rest :: []
    -> (color |> String.trim), (rest |> String.trim |> Str.split (Str.regexp ", "))
  | _ -> failwith "splitaj napaka"
(*  *)
let odstrani_nepotrebno (color, rest) =
    let f string = (string
      |> (Str.global_replace (Str.regexp "[1-5] ") "")
      |> (Str.global_replace (Str.regexp " bags") "")
      |> (Str.global_replace (Str.regexp " bag") ""))
    in
    let sez = (List.map f rest) in
    let new_sez = match sez with
      | x :: [] when x = "no other" -> []
      | _ -> sez
    in
    (color, new_sez)
(*  *)
let rec pridobi_barve list color = (* list je celoten input *)
  match list with
    | (barva, sez) :: _ when barva = color -> sez
    | _ :: tail -> pridobi_barve tail color
    | [] ->
      print_endline color;
      failwith "napaka pridobi_barve"
(*  *)
let naredi_seznam_parov_vseh_podbarv list = (* list je celoten input v parih *)
  let rec podbarve_vsake_barve acc sez =
  match sez with
    | [] -> acc
    | z :: [] when z = "no other" -> []
    | b :: bs ->
      podbarve_vsake_barve ((pridobi_barve list b) @ acc) bs
  in
  let rec aux_make acc_pairs = function
    | [] -> acc_pairs
    | (barva, sez) :: tail ->
      aux_make ((barva, sez @ (podbarve_vsake_barve [] sez)) :: acc_pairs) tail
  in
  aux_make [] list
(*  *)
let rec naredi_n_krat n list =
  if n > 1 then naredi_n_krat (n - 1) (naredi_seznam_parov_vseh_podbarv list)
  else (* n = 1 *) naredi_seznam_parov_vseh_podbarv list
(*  *)
let prestej_b_ki_vsebujejo_shinygold list = (* list celoten input *)
  let rec prestej_aux counter = function
    | [] -> counter
    | (_, bs) :: pairs ->
      if List.mem "shiny gold" bs then prestej_aux (counter + 1) pairs
      else prestej_aux counter pairs
  in
  prestej_aux 0 list
(*  *)


let naloga1 vsebina_datoteke =
  let s = vsebina_datoteke
    |> String.trim
    |> String.split_on_char '\n'
    |> List.map (Str.global_replace (Str.regexp "bags contain") ":")
    |> List.map (Str.global_replace (Str.regexp "\\.") "")
    |> List.map (String.split_on_char ':')
    |> List.map splitaj
    |> List.map odstrani_nepotrebno
    (* na tem mestu: ('barva * barva list') list *)
    |> naredi_n_krat 3
    (* na tem mestu: ('barva * barva list' list), z vsemi barvami n. reda *)
    (* 1: 16, 2: 65, 3: 144, 4: 144, skupaj barv: 594 *)

    |> prestej_b_ki_vsebujejo_shinygold
    |> string_of_int
  in
  print_endline ("day " ^ day ^ ", puzzle 1: " ^ s);
  s
(*  *)


let odstrani_nepotrebno2 (color, rest) =
    let f string = (string
      |> (Str.global_replace (Str.regexp " bags") "")
      |> (Str.global_replace (Str.regexp " bag") ""))
    in
    let sez = (List.map f rest) in
    let new_sez = match sez with
      | x :: [] when x = "no other" -> []
      | _ -> sez
    in
    (color, new_sez)
(*  *)
let barve_v_tuple (b, bs) =
  let f st_in_barva = (
    String.sub st_in_barva 0 1,
    String.sub st_in_barva 2 (String.length st_in_barva - 2)
  ) in
  (b, List.map f bs)
(*  *)
let rec get_subcols_from_col color list = (* celoten input v parih *) (* identična fukncija je napisana že prej, 'pridobi_barve' *)
  match list with
    | [] -> failwith "get_subcols_from_col napaka"
    | (barva, barve) :: _ when barva = color -> barve
    | _ :: tail -> get_subcols_from_col color tail
(*  *)
let rec prestej_vrece (color, subcolors) list = (* celoten input v parih *)
  let prestej_barvo sub =
    let (n, scolor) = sub in
    let scolors = get_subcols_from_col scolor list in
    (int_of_string n) * prestej_vrece (scolor, scolors) list
  in
  let rec prestej_vse_podbarve = function
    | [] -> 0
    | sub :: subs ->
      prestej_barvo sub + prestej_vse_podbarve subs
  in
  1 + prestej_vse_podbarve subcolors
(*  *)
let rec get_shinygold_pair = function (* v pair input listu *)
  | [] -> failwith "get_shinygold_pair napaka"
  | (b, sez) :: _ when b = "shiny gold" -> (b, sez)
  | _ :: tail -> get_shinygold_pair tail
(*  *)


let naloga2 vsebina_datoteke =
  let pair_list = vsebina_datoteke
    |> String.trim
    |> String.split_on_char '\n'
    |> List.map (Str.global_replace (Str.regexp "bags contain") ":")
    |> List.map (Str.global_replace (Str.regexp "\\.") "")
    |> List.map (String.split_on_char ':')
    |> List.map splitaj
    |> List.map odstrani_nepotrebno2
    |> List.map barve_v_tuple
  in
  let shinygold_pair = get_shinygold_pair pair_list in
  let s1 = (prestej_vrece shinygold_pair pair_list) in
  let s = s1 - 1 |> string_of_int in (* - 1, ker štejemo zraven tudi shiny gold bag *)
  print_endline ("day " ^ day ^ ", puzzle 2: " ^ s);
  s
(*  *)


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

  let vsebina_datoteke = preberi_datoteko ("2020/data/day_" ^ day ^ ".in") in
  let odgovor1 = naloga1 vsebina_datoteke in
  let odgovor2 = naloga2 vsebina_datoteke in

  izpisi_datoteko ("2020/out/day_" ^ day ^ "_1.out") odgovor1;
  izpisi_datoteko ("2020/out/day_" ^ day ^ "_2.out") odgovor2
(*  *)


(*
Day 7 summary:
https://img.ifunny.co/images/b975c23e98b38578ea483d4005ad1d6de451a6e2b57274b92dd36a6e8e78d682_1.jpg
Well, it isn't that bad. Some parts of code are awful and some are pretty sweet. :)
*)