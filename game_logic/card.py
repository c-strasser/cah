import json


class Card:
    def __init__(self, shelf_deck) -> None:
        super().__init__()
        self.shelf_deck = shelf_deck


class WhiteCard(Card):
    def __init__(self, shelf_deck, text) -> None:
        super().__init__(shelf_deck)
        self.text = text


class BlackCard(Card):
    def __init__(self, shelf_deck, text, pick) -> None:
        super().__init__(shelf_deck)
        self.text = text
        self.pick = pick
        self.chunks = self.split_into_chunks()

    def split_into_chunks(self):
        raw_chunks = self.text.split('_')
        processed_chunks = [chunk.strip() for chunk in raw_chunks]
        return processed_chunks


def load_all_packs(pack_file_path):
    """
    Load all packs contained in provided file
    :param str pack_file_path: Path to the file containting all packs
    :return: All white cards and all black cards
    :rtype: list(WhiteCard), list(BlackCard)
    """
    all_white_cards, all_black_cards = [], []
    all_data = import_data_from_json(pack_file_path)
    packs = all_data['order']
    for pack in packs:
        white_cards_in_pack, black_cards_in_pack = load_pack(all_data, pack)
        all_white_cards.extend(white_cards_in_pack)
        all_black_cards.extend(black_cards_in_pack)
    return all_white_cards, all_black_cards


def import_data_from_json(pack_file_path):
    """
    Import data from json file
    :param str pack_file_path: Path to file
    :return: Data from json file
    :rtype: dict
    """
    with open(pack_file_path) as file:
        data = json.load(file)
    return data


def load_pack(data, pack):
    """
    Load all cards from provided pack
    :param dict data: Data containing all cards for all packs
    :param str pack: Name of the pack to load
    :return: White cards and black cards from provided pack
    :rtype: list(WhiteCard), list(BlackCard)
    """
    pack_name, white_indexes, black_indexes = data[pack]['name'], data[pack]['white'], data[pack]['black']
    white_cards = [process_white_card(pack_name, raw_card)
                   for i, raw_card in enumerate(data['whiteCards']) if i in white_indexes]
    black_cards = [process_black_card(pack_name, raw_card)
                   for i, raw_card in enumerate(data['blackCards']) if i in black_indexes]
    return white_cards, black_cards


def process_white_card(pack_name, raw_card):
    """
    Process white card from raw data:
        - assign text
        - assign name of pack
    :param str pack_name
    :param str raw_card: Text from the white card
    :return: Processed white card
    :rtype: WhiteCard
    """
    new_card = WhiteCard(pack_name, raw_card)
    return new_card


def process_black_card(pack_name, raw_card):
    """
    Process black card from raw data:
        - assign text
        - assign name of pack
        - Number of cards to pick
    :param str pack_name
    :param str raw_card: Text from the white card
    :return: Processed white card
    :rtype: WhiteCard
    """
    new_card = BlackCard(pack_name, raw_card['text'], raw_card['pick'])
    return new_card
