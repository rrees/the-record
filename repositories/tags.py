import filecabinet

def dossiers_with_tag(user, tag_name):
	return [d for d in filecabinet.Dossier.query().filter(filecabinet.Dossier.user == user).filter(filecabinet.Dossier.tags.IN([tag_name]))]
